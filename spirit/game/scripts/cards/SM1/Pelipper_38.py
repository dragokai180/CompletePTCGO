from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae533409-ddf6-5391-ab67-6de377239f51',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name',
    display_name='Pelipper',
    searchable_by=['Pelipper', 'Stage 1', 'Pelipper'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name',
    family_id=278,
    abilities=[
        Attack(
            title='Courier',
            game_text='Put 1 of your Benched Pokémon and all cards attached to it into your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Fly',
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
