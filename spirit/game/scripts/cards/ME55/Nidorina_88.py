from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1972a25f-b6c2-50e2-ba4f-f5349490b718',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    display_name='Nidorina',
    searchable_by=['Nidorina', 'Stage 1', 'Nidorina'],
    subtypes=['Stage 1'],
    collector_number=88,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    family_id=29,
    abilities=[
        Ability(
            title='Share Happiness',
            game_text='Once during your turn, you may use this Ability. Heal 30 damage from 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
