from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import heal_attack, recover_from_discard, requires_discard
from spirit.game.session.effects import is_item_card

pickup = recover_from_discard(
    predicate=is_item_card, count=1, minimum=1, reveal=False, to="hand",
    prompt="Choose an Item card to put into your hand.",
)

card = PokemonCardDef(
    guid="2636f1ae-8bc8-505a-81b7-6895e963e24a",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup","Basic","Lillipup"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Pickup",
            game_text="Put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pickup,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
