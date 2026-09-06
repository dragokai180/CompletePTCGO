from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage, condition_attack

card = PokemonCardDef(
    guid="657e93a8-b04d-5d3c-868d-8aeff41a760f",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGolisopodex.Name",
    display_name="Mega Golisopod ex",
    searchable_by=["Mega Golisopod ex","Stage 1","ex","SV_Mega","MegaGolisopodex"],
    subtypes=["Stage 1","ex","SV_Mega"],
    collector_number=9,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Finishing Blow",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 160 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(has_damage(), 160),
        ),
        Attack(
            title="Quattro Hold",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
