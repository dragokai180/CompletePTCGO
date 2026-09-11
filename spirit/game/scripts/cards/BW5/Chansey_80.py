from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy

card = PokemonCardDef(
    guid="a5f1c5d9-e903-5629-b48c-44a153234f28",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey","Basic","Chansey"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Sing",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=powder_snow,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=recoil_attack(30),
        ),
    ],
)
