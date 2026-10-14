"""Mapa de Europa (Natural Earth, dominio público) proyectado en Mercator para el lienzo 400 × 700."""
import json, math, os
D = os.path.dirname(os.path.abspath(__file__))
LON0, LON1, LAT1 = -14.5, 17.5, 62.0
K = 400 / math.radians(LON1 - LON0)
merc = lambda la: math.log(math.tan(math.pi / 4 + math.radians(la) / 2))
def proj(lon, lat): return ((lon - LON0) * math.pi / 180 * K, (merc(LAT1) - merc(lat)) * K)

def dp(pts, tol):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]; dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1e-9
    i, dm = 0, -1
    for j in range(1, len(pts) - 1):
        d = abs(dy * pts[j][0] - dx * pts[j][1] + b[0] * a[1] - b[1] * a[0]) / L
        if d > dm: i, dm = j, d
    return dp(pts[:i + 1], tol)[:-1] + dp(pts[i:], tol) if dm > tol else [a, b]

def clip(ring, x0=-8, y0=-8, x1=408, y1=708):
    def cut(pts, inside, inter):
        out = []
        for i in range(len(pts)):
            a, b = pts[i - 1], pts[i]
            if inside(b):
                if not inside(a): out.append(inter(a, b))
                out.append(b)
            elif inside(a): out.append(inter(a, b))
        return out
    lerp = lambda a, b, t: (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    for inside, inter in ((lambda p: p[0] >= x0, lambda a, b: lerp(a, b, (x0 - a[0]) / (b[0] - a[0]))),
                          (lambda p: p[0] <= x1, lambda a, b: lerp(a, b, (x1 - a[0]) / (b[0] - a[0]))),
                          (lambda p: p[1] >= y0, lambda a, b: lerp(a, b, (y0 - a[1]) / (b[1] - a[1]))),
                          (lambda p: p[1] <= y1, lambda a, b: lerp(a, b, (y1 - a[1]) / (b[1] - a[1])))):
        ring = cut(ring, inside, inter)
        if not ring: break
    return ring

def country_paths(tol=.9):
    d = json.load(open(os.path.join(D, 'ne_50m_admin_0_countries.geojson')))
    out = {}
    for f in d['features']:
        name = f['properties']['NAME_EN'] if 'NAME_EN' in f['properties'] else f['properties']['NAME']
        g = f['geometry']; polys = [g['coordinates']] if g['type'] == 'Polygon' else g['coordinates']
        segs = []
        for poly in polys:
            ring = [proj(lo, la) for lo, la in poly[0]]
            xs = [p[0] for p in ring]; ys = [p[1] for p in ring]
            if max(xs) < -40 or min(xs) > 440 or max(ys) < -40 or min(ys) > 740: continue
            ring = clip(ring)
            if len(ring) < 4: continue
            k = max(range(len(ring)), key=lambda j: (ring[j][0] - ring[0][0]) ** 2 + (ring[j][1] - ring[0][1]) ** 2)
            r = dp(ring[:k + 1], tol)[:-1] + dp(ring[k:], tol)
            if len(r) < 4: continue
            segs.append('M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in r) + 'Z')
        if segs: out[name] = ''.join(segs)
    return out

if __name__ == '__main__':
    p = country_paths(); print(len(p), sum(len(v) for v in p.values()), sorted(p)[:60])
    print({c: tuple(round(v) for v in proj(*ll)) for c, ll in dict(Roma=(12.5, 41.9), Madrid=(-3.7, 40.4), Parigi=(2.35, 48.85), Berlino=(13.4, 52.5), Londra=(-0.13, 51.5), Lisbona=(-9.14, 38.72)).items()})
