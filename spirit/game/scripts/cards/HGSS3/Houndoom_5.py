from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d71b1a76-47ce-55ed-a3c3-03733e295571',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name',
    display_name='Houndoom',
    searchable_by=['Houndoom', 'Stage 1', 'Houndoom'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    family_id=228,
    abilities=[
        Attack(
            title='Fire Counterattack',
            game_text='If your opponent has any Fighting Pokémon in play, this attack does 20 damage plus 60 more damage.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dark Roar',
            game_text='Your opponent discards a card from his or her hand.',
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
