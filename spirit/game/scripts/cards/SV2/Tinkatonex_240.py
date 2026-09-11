from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6d976c0-6425-5097-9cec-0c78ad81de42',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatonex.Name',
    display_name='Tinkaton ex',
    searchable_by=['Tinkaton ex', 'Stage 2', 'ex', 'Tinkatonex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=240,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareUltra,
    hp=300,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name',
    family_id=957,
    abilities=[
        Attack(
            title='Big Hammer',
            game_text='This attack does 30 damage for each card in your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Pulverizing Press',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
