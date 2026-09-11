from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c2ab2388-8d93-5255-9415-d669e729b781',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiningGenesect.Name',
    display_name='Shining Genesect',
    searchable_by=['Shining Genesect', 'Basic', 'ShiningGenesect'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Shining,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=649,
    abilities=[
        Ability(
            title='Energy Reload',
            game_text='Once during your turn (before your attack), you may move a Grass Energy from 1 of your other Pokémon to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Gaia Blaster',
            game_text='This attack does 20 more damage times the amount of Grass Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
