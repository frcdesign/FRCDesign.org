/**
 * Glossary of terms and abbreviations
 *
 * Add terms here to automatically highlight them across the site
 * with a dotted underline and hover tooltip.
 *
 * Format:
 * {
 *   term: "TERM",           // The word/abbreviation to match (case-insensitive)
 *   definition: "..."       // The explanation shown on hover
 * }
 */

export interface GlossaryTerm {
  term: string;
  definition: string;
}

export const glossaryTerms: GlossaryTerm[] = [
  // Vendors
  {
    term: "WCP",
    definition: "West Coast Products"
  },
  {
    term: "REV",
    definition: "REV Robotics"
  },
  {
    term: "TTB",
    definition: "The Thrifty Bot"
  },
  {
    term: "Redux",
    definition: "Redux Robotics"
  },
  {
    term: "MCM",
    definition: "McMaster Carr"
  },

  // Intake styles
  {
    term: "OTB",
    definition: "\"Over the Bumper\" - A style of intake where you lift the piece over the bumper"
  },
  {
    term: "UTB",
    definition: "\"Under the Bumper\" - A style of intake where you move the piece under the bumper"
  },

  // Parts & Components
  {
    term: "COTS",
    definition: "Commercial Off the Shelf - Parts you can buy from a vendor"
  },
  {
    term: "V4B",
    definition: "\"Virtual 4 Bar\" - Where a second degree of freedom is directly geared off a previous degree of freedom instead of being moved independently or by a linkage"
  },
  {
    term: "C-C",
    definition: "\"Center to Center\" distance"
  },
  {
    term: "turnbuckle",
    definition: "A threaded part that goes in between chain links to tension the chain"
  },
  {
    term: "4Bar",
    definition: "A type of linkage characterized by its 4 pivot points"
  },
  {
    term: "Tube-Nut",
    definition: "Also known as a \"Star Nut\" - Provides an easy way to put a thread in end of a hollow tube allowing you to bolt the tube to another part"
  },
  {
    term: "Gusset",
    definition: "Reinforcement plate, usually made of aluminum, used to strengthen connections between two tubes"
  },

  // Physics & Engineering concepts
  {
    term: "COG",
    definition: "Center of Gravity, also referred to as COM (Center of Mass)"
  },
  {
    term: "Cantilever",
    definition: "Horizontal element that's supported by one side only"
  },
  {
    term: "Shear",
    definition: "When forces are applied parallel to the plane of a material, causing breaking of fasteners due to excessive force and stress"
  },
  {
    term: "Torque",
    definition: "Force that produces rotational movement"
  },
  {
    term: "DP",
    definition: "Diametral pitch - The number of teeth per inch of the pitch circle"
  },
  {
    term: "Backlash",
    definition: "'Slop' in a power transmission system; can wiggle back and forth without engaging the whole system"
  },

  // Axle types
  {
    term: "Deadaxle",
    definition: "A type of axle setup where the axle is fixed in place and/or is not transferring the torque of the system through it"
  },
  {
    term: "Liveaxle",
    definition: "A type of axle setup where the main torque transfer is through the axle"
  },
  {
    term: "Zombie-Axle",
    definition: "Typically used on pivots - A zombie axle spins with the mechanism, but is transferring little to no torque through it. Commonly used to put an encoder on the pivot point"
  },

  // Electronics
  {
    term: "PDH",
    definition: "Power Distribution Hub"
  },
  {
    term: "SparkMAX",
    definition: "Motor controller for REV motors"
  },
  {
    term: "PWM",
    definition: "Pulse Width Modulation cable"
  },
  {
    term: "RIO",
    definition: "roboRIO - The brain of the robot"
  },
  {
    term: "Blinkin",
    definition: "LED controller for REV"
  },
  {
    term: "Radio",
    definition: "Device that helps the robot communicate with the driver station"
  },

  // Manufacturing & Materials
  {
    term: "3DP",
    definition: "Abbreviation for 3D printed or 3D printing"
  },
  {
    term: "Poly",
    definition: "Abbreviation for polycarbonate"
  },
  {
    term: "PC",
    definition: "Abbreviation for polycarbonate"
  },
  {
    term: "Stripping",
    definition: "Process of removing threads or bolt heads, often due to excessive force or wear"
  },
  {
    term: "Tapping",
    definition: "The process of creating threads in a hole using a tap tool"
  },
  {
    term: "Billet",
    definition: "Component machined down from a solid block of material"
  },

  // Robot structure
  {
    term: "Brainpan",
    definition: "Flipped electronics bellypan"
  },
  {
    term: "Bellypan",
    definition: "Plate for mounting electronics on the underside of your drivebase"
  },
  {
    term: "Hardstop",
    definition: "A physical limit designed to prevent a mechanism or component from moving beyond a certain point"
  },
  {
    term: "Softstop",
    definition: "A software-based limit or control mechanism that restricts the movement of a mechanism or component to prevent it from exceeding certain parameters"
  },

  // Design concepts
  {
    term: "Packaging",
    definition: "The way in which you fit parts of your robot together in a space"
  },
  {
    term: "Parametric",
    definition: "Designed in a way that uses relationships between steps to maintain design intent"
  },
];

/**
 * Get a glossary term by its name (case-insensitive)
 */
export function getGlossaryTerm(term: string): GlossaryTerm | undefined {
  return glossaryTerms.find(g => g.term.toLowerCase() === term.toLowerCase());
}

/**
 * Get all terms as a map for quick lookup
 */
export function getGlossaryMap(): Map<string, string> {
  const map = new Map<string, string>();
  glossaryTerms.forEach(({ term, definition }) => {
    map.set(term.toLowerCase(), definition);
  });
  return map;
}
