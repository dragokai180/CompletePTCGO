from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bddc7d53-626a-5beb-8bf0-bf1381e6e1bb',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espeonex.Name',
    display_name='Espeon ex',
    searchable_by=['Espeon ex', 'Stage 1', 'ex', 'Espeonex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=70,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Solar Beatdown',
            game_text='This attack does 30 damage for each of your Pokémon in play.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
