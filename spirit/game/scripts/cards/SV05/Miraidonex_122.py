from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="a35e541a-9ed0-5af1-8dad-63d79df39be5",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Future", "Miraidonex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=122,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=1008,
    abilities=[
        Attack(
            title="Repulsion Bolt",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Cyber Drive",
            game_text="During your next turn, this Pokémon can't use Cyber Drive.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
