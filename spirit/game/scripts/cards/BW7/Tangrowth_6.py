from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="1d9e3268-afee-500e-b558-d352b7dce346",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth","Stage 1","Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    abilities=[
        Attack(
            title="Hundred Furious Lashes",
            game_text="Does 30 damage times the amount of Grass Energy attached to this Pokémon. This Pokémon can't use Hundred Furious Lashes during your next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=heal_attack(30),
        ),
    ],
)
