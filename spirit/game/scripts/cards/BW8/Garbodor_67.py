from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2bd7187d-e1f2-5d62-8dd0-145b394023a9",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor","Stage 1","Garbodor","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=67,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    abilities=[
        Attack(
            title="Ensnarl",
            game_text="Does 20 damage times the number of Colorless in the Defending Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Double Ducts",
            game_text="Flip 2 coins. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=80),
        ),
    ],
)
