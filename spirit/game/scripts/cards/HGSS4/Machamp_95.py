from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='278a4f09-6b6a-50d3-837a-6677b605c617',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name',
    display_name='Machamp',
    searchable_by=['Machamp', 'Stage 2', 'Prime', 'Machamp'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=95,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name',
    family_id=66,
    abilities=[
        Ability(
            title='Fighting Tag',
            game_text='Once during your turn (before your attack), if Machamp is on your Bench, you may move all Fighting Energy attached to your Active Pokémon to Machamp. If you do, switch Machamp with your Active Pokémon.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Crushing Punch',
            game_text='Discard a Special Energy card attached to the Defending Pokémon.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Champ Buster',
            game_text='Does 100 damage plus 10 more damage for each of your Benched Pokémon that has any damage counters on it.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
