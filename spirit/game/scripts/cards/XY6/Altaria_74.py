from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c000f05-df56-5ba1-bc08-7b3156365cc3',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name',
    display_name='Altaria',
    searchable_by=['Altaria', 'Stage 1', 'Altaria'],
    subtypes=['Stage 1'],
    collector_number=74,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    family_id=333,
    abilities=[
        Ability(
            title='Clear Humming',
            game_text='Each of your Colorless Pokémon has no Weakness.',
            passive=standard_passive('Each of your Colorless Pokémon has no Weakness.'),
        ),
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
    passive=standard_passive('You may play this card from your hand to evolve a Pokémon during your first turn or the turn you play that Pokémon.'),
)
