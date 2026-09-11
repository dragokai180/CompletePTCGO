from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="cea2d7de-f836-5e2a-9f2e-e218b9903404",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HearthflameMaskOgerpon.Name",
    display_name="Hearthflame Mask Ogerpon",
    searchable_by=["Hearthflame Mask Ogerpon", "Basic", "HearthflameMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=1017,
    abilities=[
        Attack(
            title="Fire Kagura",
            game_text="Search your deck for a Basic Fire Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
