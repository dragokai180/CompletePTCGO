from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee894c89-4781-52b4-9628-bcc814474683',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name',
    display_name='Clefable',
    searchable_by=['Clefable', 'Stage 1', 'Clefable'],
    subtypes=['Stage 1'],
    collector_number=3,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    family_id=35,
    abilities=[
        Attack(
            title='Fairy Power',
            game_text='Return 1 of your Pokémon and all cards attached to it to your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Moon Impact',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
