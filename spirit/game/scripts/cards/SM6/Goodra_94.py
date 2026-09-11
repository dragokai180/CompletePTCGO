from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c07a378f-e7bb-5dde-90e3-de9e09e1ebc1',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name',
    display_name='Goodra',
    searchable_by=['Goodra', 'Stage 2', 'Goodra'],
    subtypes=['Stage 2'],
    collector_number=94,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name',
    family_id=704,
    abilities=[
        Ability(
            title='Hydration',
            game_text='Whenever you attach a Water Energy card from your hand to this Pokémon, heal 20 damage from it.',
            passive=standard_passive('Whenever you attach a Water Energy card from your hand to this Pokémon, heal 20 damage from it.'),
        ),
        Attack(
            title='Soaking Horn',
            game_text='If this Pokémon was healed during this turn, this attack does 80 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
