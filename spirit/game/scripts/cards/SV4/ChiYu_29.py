from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7cdfeb87-53a4-526b-8b17-87f653ff1b3c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name',
    display_name='Chi-Yu',
    searchable_by=['Chi-Yu', 'Basic', 'ChiYu'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=1004,
    abilities=[
        Attack(
            title='Flare Bringer',
            game_text='Attach up to 2 Basic Fire Energy cards from your discard pile to 1 of your Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Megafire of Envy',
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
