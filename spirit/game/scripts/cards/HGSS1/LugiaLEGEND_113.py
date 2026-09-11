from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1a06a4e4-3e94-5693-b3cc-aaf52c558a2f',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LugiaLEGEND.Name',
    display_name='Lugia LEGEND',
    searchable_by=['Lugia LEGEND', 'LEGEND', 'LugiaLEGEND'],
    subtypes=['LEGEND'],
    collector_number=113,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.LEGEND,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Ability(
            title='Ocean Grow',
            game_text='Once during your turn, when you put Lugia LEGEND into play, you may look at the top 5 cards of your deck and attach all Energy cards you find there to Lugia LEGEND. Discard the other cards.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Elemental Blast',
            game_text='Discard a Fire Energy, Water Energy, and Lightning Energy attached to Lugia LEGEND.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
