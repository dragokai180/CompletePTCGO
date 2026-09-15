from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import call_for_family, comet_punch

card = PokemonCardDef(
    guid="a33e0208-4c25-5ecb-ab0f-760388d221d9",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name",
    display_name="Emolga",
    searchable_by=["Emolga","Basic","Emolga"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=call_for_family,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)
