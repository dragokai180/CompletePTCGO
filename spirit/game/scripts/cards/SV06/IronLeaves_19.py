from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="46049834-662b-56d5-bc1f-fed3023c9c69",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronLeaves.Name",
    display_name="Iron Leaves",
    searchable_by=["Iron Leaves", "Basic", "Future", "IronLeaves"],
    subtypes=["Basic", "Future"],
    collector_number=19,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=1010,
    abilities=[
        Attack(
            title="Recovery Net",
            game_text="Put up to 2 Pokémon from your discard pile into your hand.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Avenging Edge",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
