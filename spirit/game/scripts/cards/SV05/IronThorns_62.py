from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2a87e668-49fc-5a4d-a66a-51a9b2feb146",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronThorns.Name",
    display_name="Iron Thorns",
    searchable_by=["Iron Thorns", "Basic", "Future", "IronThorns"],
    subtypes=["Basic", "Future"],
    collector_number=62,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=995,
    abilities=[
        Attack(
            title="Destructo-Press",
            game_text="Reveal the top 5 cards of your deck. This attack does 70 damage for each Future card you find there. Then, discard those Future cards and shuffle the other cards back into your deck.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Megaton Lariat",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
