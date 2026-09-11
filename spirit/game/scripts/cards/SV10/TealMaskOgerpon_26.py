from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="c9188ad1-8c26-5630-8f0a-4355fb28b12f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerpon.Name",
    display_name="Teal Mask Ogerpon",
    searchable_by=["Teal Mask Ogerpon", "Basic", "TealMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=1017,
    abilities=[
        Attack(
            title="Grass Kagura",
            game_text="Search your deck for a Basic Grass Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Ogre's Hammer",
            game_text="During your next turn, this Pokémon can't use Ogre's Hammer.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
