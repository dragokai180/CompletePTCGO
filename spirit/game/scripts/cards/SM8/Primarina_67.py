from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6666eb92-1c45-553f-8d1f-0b73aa85f4ff',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Primarina.Name',
    display_name='Primarina',
    searchable_by=['Primarina', 'Stage 2', 'Primarina'],
    subtypes=['Stage 2'],
    collector_number=67,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name',
    family_id=728,
    abilities=[
        Ability(
            title='Harmonics',
            game_text='Whenever you attach an Energy card from your hand to 1 of your Pokémon, except with an attack, Ability, or Trainer card, attach up to 2 Energy cards to that Pokémon instead of 1.',
            passive=standard_passive('Whenever you attach an Energy card from your hand to 1 of your Pokémon, except with an attack, Ability, or Trainer card, attach up to 2 Energy cards to that Pokémon instead of 1.'),
        ),
        Attack(
            title='Hypno Splash',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
