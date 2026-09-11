from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd15f85a-c663-5439-ac69-1d0249dd1de4',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name',
    display_name='Reshiram',
    searchable_by=['Reshiram', 'Basic', 'Reshiram'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=643,
    abilities=[
        Ability(
            title='Turboblaze',
            game_text='Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may attach a Fire Energy card from your hand to 1 of your Dragon Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Bright Wing',
            game_text='Discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
