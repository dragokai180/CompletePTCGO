from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8f86486a-dd36-5465-b001-27eebb474ebd',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name',
    display_name='Luxio',
    searchable_by=['Luxio', 'Stage 1', 'Luxio'],
    subtypes=['Stage 1'],
    collector_number=70,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name',
    family_id=403,
    abilities=[
        Attack(
            title='Zap Kick',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title='Head Bolt',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
