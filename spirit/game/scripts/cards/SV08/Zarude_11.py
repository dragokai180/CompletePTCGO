from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="3387db38-6d91-536d-9d1b-edac25c8d752",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic", "Zarude"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=893,
    abilities=[
        Attack(
            title="Leaf Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Jungle Whip",
            game_text="You may put all Energy attached to this Pokémon into your hand to have this attack do 80 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
