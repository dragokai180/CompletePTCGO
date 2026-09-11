from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2444b73c-4375-5841-840a-e000a025602f',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name',
    display_name='Salazzle',
    searchable_by=['Salazzle', 'Stage 1', 'Salazzle'],
    subtypes=['Stage 1'],
    collector_number=99,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    family_id=757,
    abilities=[
        Attack(
            title='Smack',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
        ),
        Attack(
            title='Slashing Claw',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
