from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec1c7626-b1b7-5c53-811d-2721c0b2a821',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name',
    display_name='Miraidon ex',
    searchable_by=['Miraidon ex', 'Basic', 'ex', 'Miraidonex'],
    subtypes=['Basic', 'ex'],
    collector_number=79,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=1008,
    abilities=[
        Attack(
            title='Rapid Draw',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Techno Turbo',
            game_text='Attach a Basic Lightning Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
