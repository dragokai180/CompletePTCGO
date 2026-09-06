from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


def _ten_or_more_in_hand(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) >= 10


card = PokemonCardDef(
    guid="992154c4-9c95-56a0-a6d4-33d7766d7662",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGolurkex.Name",
    display_name="Mega Golurk ex",
    searchable_by=["Mega Golurk ex","Stage 1","ex","SV_Mega","MegaGolurkex"],
    subtypes=["Stage 1","ex","SV_Mega"],
    collector_number=33,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Ability(
            title="Movement Restriction",
            game_text="This Pokémon can't attack unless you have 10 or more cards in your hand.",
        ),
        Attack(
            title="Goliath Punch",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=300,
            condition=_ten_or_more_in_hand,
            effect=recoil_attack(30),
        ),
    ],
)
