from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d54cefe1-f675-5d79-99b8-a6865eb8834d',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name',
    display_name='Silvally-GX',
    searchable_by=['Silvally-GX', 'Stage 1', 'GX', 'SilvallyGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=184,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name',
    family_id=772,
    abilities=[
        Ability(
            title='Disk Reload',
            game_text='Once during your turn (before your attack), you may draw cards until you have 5 cards in your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Brave Buddies',
            game_text='If you played a Supporter card from your hand during this turn, this attack does 70 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Silver Knight-GX',
            game_text="If your opponent's Active Pokémon is an Ultra Beast, it is Knocked Out. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
