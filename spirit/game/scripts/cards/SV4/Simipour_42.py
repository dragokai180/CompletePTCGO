from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='545b26f3-b64d-54a6-bc17-902da7f9a26e',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name',
    display_name='Simipour',
    searchable_by=['Simipour', 'Stage 1', 'Simipour'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name',
    family_id=515,
    abilities=[
        Ability(
            title='Monkey Trio',
            game_text='If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.',
            passive=standard_passive('If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.'),
        ),
        Attack(
            title='Liquid Lashing',
            game_text="This attack also does 30 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
