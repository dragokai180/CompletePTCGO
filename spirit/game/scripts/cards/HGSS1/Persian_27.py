from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='00e90c93-5a07-5d3a-9646-1041eb025f92',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name',
    display_name='Persian',
    searchable_by=['Persian', 'Stage 1', 'Persian'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    family_id=52,
    abilities=[
        Attack(
            title='Sharpen Claws',
            game_text="Flip 3 coins. For each heads, discard a card from your opponent's hand without looking.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sneaky Attack',
            game_text='If Persian has any Darkness Energy attached to it, this attack does 30 damage plus 30 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
