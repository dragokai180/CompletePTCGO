from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_ex
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.models.board import PokemonEntity, PlayerEntity


def _opponent_has_pokemon_ex(pokemon, carrier):
    root = carrier
    while root.parent is not None:
        root = root.parent
    for player in root.children:
        if not isinstance(player, PlayerEntity):
            continue
        if player.owning_player_id == carrier.owning_player_id:
            continue
        for area in player.children:
            for card in getattr(area, "children", []):
                if isinstance(card, PokemonEntity) and is_pokemon_ex(card.archetype_id):
                    return True
    return False


card = PokemonCardDef(
    guid="94aee694-8040-57b1-b77b-b5ca9d55beb7",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod","Basic","Wimpod"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=767,
    abilities=[
        Ability(
            title="Punk Out",
            game_text="If your opponent has a Pokémon ex in play, this Pokémon has no Retreat Cost.",
            passive=retreat_free_when(_opponent_has_pokemon_ex),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
