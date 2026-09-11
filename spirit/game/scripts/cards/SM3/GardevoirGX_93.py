from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='235eef2d-84bd-54da-9612-71d50add0327',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirGX.Name',
    display_name='Gardevoir-GX',
    searchable_by=['Gardevoir-GX', 'Stage 2', 'GX', 'GardevoirGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=93,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=230,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    family_id=280,
    abilities=[
        Ability(
            title='Secret Spring',
            game_text='Once during your turn (before your attack), you may attach a Fairy Energy card from your hand to 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Infinite Force',
            game_text='This attack does 30 damage times the amount of Energy attached to both Active Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Twilight-GX',
            game_text="Shuffle 10 cards from your discard pile into your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
