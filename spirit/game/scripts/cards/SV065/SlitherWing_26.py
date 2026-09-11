from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="22577a35-cc76-5a90-b4cb-f167b501ee10",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlitherWing.Name",
    display_name="Slither Wing",
    searchable_by=["Slither Wing", "Basic", "Ancient", "SlitherWing"],
    subtypes=["Basic", "Ancient"],
    collector_number=26,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=988,
    abilities=[
        Attack(
            title="Iron Smasher",
            game_text="If your opponent has any Future Pokémon in play, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Smashing Wing",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
