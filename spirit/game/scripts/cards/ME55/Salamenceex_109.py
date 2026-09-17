from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='38cbe18f-9c1d-5826-a724-0b2c593e6508',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name',
    display_name='Salamence ex',
    searchable_by=['Salamence ex', 'Stage 2', 'ex', 'Salamenceex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=109,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name',
    family_id=373,
    abilities=[
        Attack(
            title='Booming Call',
            game_text='Put up to 3 Dragon Pokémon from your discard pile onto your Bench.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top 2 cards of your deck.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=240,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
