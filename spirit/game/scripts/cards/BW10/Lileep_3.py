from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.bw10 import prehistoric_call, spiral_drain_10

card = PokemonCardDef(
    guid="d7557a9d-064d-57cf-a4cd-93b75593ff05",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Restored", "Lileep"],
    subtypes=["Restored"],
    collector_number=3,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.RESTORED,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RootFossilLileep.Name",
    family_id=345,
    unplayable_from_hand=True,
    abilities=[
        Ability(
            title="Prehistoric Call",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put this Pok\u00e9mon on the bottom of your deck.",
            effect=prehistoric_call,
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=spiral_drain_10,
        ),
    ],
)
