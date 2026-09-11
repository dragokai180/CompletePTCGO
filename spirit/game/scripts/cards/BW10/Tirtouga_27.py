from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.bw10 import prehistoric_call, slam

card = PokemonCardDef(
    guid="b989a6a5-b6c1-5ca8-9f48-998ade5470fb",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    display_name="Tirtouga",
    searchable_by=["Tirtouga", "Restored", "Tirtouga"],
    subtypes=["Restored"],
    collector_number=27,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.RESTORED,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CoverFossil.Name",
    family_id=564,
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
            title="Slam",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=slam,
        ),
    ],
)
