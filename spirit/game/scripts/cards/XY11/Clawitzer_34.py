from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ccf89052-914a-5c3b-83a0-db58f61bb20c',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name',
    display_name='Clawitzer',
    searchable_by=['Clawitzer', 'Stage 1', 'Clawitzer'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name',
    family_id=692,
    abilities=[
        Ability(
            title='Mega Boost',
            game_text='Once during your turn (before your attack), you may attach a Special Energy card from your hand to 1 of your Mega Evolution Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
