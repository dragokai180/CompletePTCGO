from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a5efd131-a663-598b-8718-c970f267e327',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name',
    display_name='Watchog',
    searchable_by=['Watchog', 'Stage 1', 'Watchog'],
    subtypes=['Stage 1'],
    collector_number=108,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name',
    family_id=504,
    abilities=[
        Attack(
            title='Scrutinize',
            game_text="Look at the top 2 cards of your opponent's deck, discard 1 of them, and put the other card back.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slam',
            game_text='Flip 2 coins. This attack does 60 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
