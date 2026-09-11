from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7d80271-36d1-525f-a427-805d60ef4083',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name',
    display_name='Tinkaton',
    searchable_by=['Tinkaton', 'Stage 2', 'Tinkaton'],
    subtypes=['Stage 2'],
    collector_number=140,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name',
    family_id=959,
    abilities=[
        Attack(
            title='Knock Off',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Wild Press',
            game_text='This Pokémon also does 60 damage to itself.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
