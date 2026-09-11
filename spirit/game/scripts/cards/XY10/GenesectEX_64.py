from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='830b7a2a-2bde-5695-a222-c783467fa64a',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name',
    display_name='Genesect-EX',
    searchable_by=['Genesect-EX', 'Basic', 'EX', 'GenesectEX'],
    subtypes=['Basic', 'EX'],
    collector_number=64,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=649,
    abilities=[
        Ability(
            title='Drive Change',
            game_text='Once during your turn (before your attack), you may put a Pokémon Tool card attached to this Pokémon into your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Rapid Blaster',
            game_text='Discard as many Metal Energy attached to this Pokémon as you like. This attack does 20 more damage for each Energy card discarded in this way.',
            cost={PokemonTypes.METAL: 3},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
