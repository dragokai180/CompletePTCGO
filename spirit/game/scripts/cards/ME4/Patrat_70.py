from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.session.passives import Passive


class WatchfulEyePassive(Passive):
    """Damage counters on each Pokémon can't be moved to other Pokémon."""

    def blocks_moving_damage_counters(self, carrier):
        return True


card = PokemonCardDef(
    guid="3323fb01-906c-51d9-8dc0-1b493ee38562",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    display_name="Patrat",
    searchable_by=["Patrat","Basic","Patrat"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=504,
    abilities=[
        Ability(
            title="Watchful Eye",
            game_text="Damage counters on each Pokémon (both yours and your opponent's) can't be moved to other Pokémon.",
            passive=WatchfulEyePassive(),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
