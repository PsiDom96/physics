class Mesh:
    def __init__(self):
        self.nodes = None
        self.elements = None
        self.dimension = None

    def plot(self):
        pass

    def refine(self):
        pass

    def coarsen(self):
        pass

    def export(self, filename):
        pass


class StructuredMesh(Mesh):

    def __init__(
        self,
        nx,
        ny,
        width,
        height
    ):
        super().__init__()

        self.nx = nx
        self.ny = ny
        self.width = width
        self.height = height

        self.nodes = self._generate_nodes()
        self.elements = self._generate_elements()

class UnstructuredMesh(Mesh):
    
    def __init__(
        self,
        nodes,
        elements,
        boundary_nodes = None,
        boundary_edges = None,
        material_regions = None,
        target_element_size = None,
    ):

        super().__init__()

        self.nodes = nodes,
        self.elements = elements
        self.target_element_size = target_element_size
        

class TriangularMesh(UnstructuredMesh):

    def __init__(
        self,
        nodes,
        triangles
    ):
        super().__init__(
            nodes = nodes,
            elements = triangles
        )
        
        self.dimension = 2


@classmethod
def from_polygon(
    cls,
    polygon,
    max_element_size
):
    nodes, triangles = triangulate(
        polygon,
        max_element_size
    )

    return cls(
        nodes,
        triangles
    )

generate_rectangular_mesh()
generate_triangular_mesh()
generate_tetrahedral_mesh()

refine_mesh()
coarsen_mesh()


mesh = StructuredMesh(
    nx=200,
    ny=200,
    width=0.5,
    height=0.5
)

mesh.refine_region(
    center=(0.25,0.25),
    radius=0.05
)

mesh.plot()

mesh = TriangularMesh.from_polygon(
    tongue_drum_outline,
    max_element_size=0.005
)

mesh.adaptive_refine(
    error_estimator="curvature"
)

