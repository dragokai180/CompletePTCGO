from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="d977cf2b-5cb7-5253-82f5-9833c054b780",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensGreedent.Name",
    display_name="Arven's Greedent",
    searchable_by=["Arven's Greedent", "Stage 1", "ArvensGreedent"],
    subtypes=["Stage 1"],
    collector_number=159,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensSkwovet.Name",
    family_id=819,
    abilities=[
        Ability(
            title="Greedy Order",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put up to 2 Arven's Sandwich cards from your discard pile into your hand.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
