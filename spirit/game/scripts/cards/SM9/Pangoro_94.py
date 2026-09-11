from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85b63d95-8414-56aa-9767-22073acf2f5b',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name',
    display_name='Pangoro',
    searchable_by=['Pangoro', 'Stage 1', 'Pangoro'],
    subtypes=['Stage 1'],
    collector_number=94,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    family_id=674,
    abilities=[
        Attack(
            title='Tighten Up',
            game_text='Your opponent discards 2 cards from their hand.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Tantrum',
            game_text='This Pokémon is now Confused.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
