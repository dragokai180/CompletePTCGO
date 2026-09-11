from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4b55e82-d4bd-53e9-8026-0947e15d13b7',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name',
    display_name='Espeon',
    searchable_by=['Espeon', 'Stage 1', 'Prime', 'Espeon'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=81,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Ability(
            title='Evolution Memories',
            game_text='Espeon can use the attacks of all Pokémon you have in play that evolve from Eevee as its own. (You still need the necessary Energy to use each attack.)',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Espeon can use the attacks of all Pokémon you have in play that evolve from Eevee as its own. (You still need the necessary Energy to use each attack.)'),
        ),
        Attack(
            title='Solar Ray',
            game_text='Remove 1 damage counter from each of your Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
