from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0a5bc41c-16db-549d-b08b-e7515dd10164',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sylveonex.Name',
    display_name='Sylveon ex',
    searchable_by=['Sylveon ex', 'Stage 1', 'ex', 'Sylveonex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=71,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Colorful Harmony',
            game_text='This attack does 50 damage for each type of Basic Energy attached to all of your Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
