from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a69e8a63-0267-5e30-bac2-c3566fcb2d2f',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name',
    display_name='Kommo-o',
    searchable_by=['Kommo-o', 'Stage 2', 'Kommoo'],
    subtypes=['Stage 2'],
    collector_number=163,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name',
    family_id=782,
    abilities=[
        Attack(
            title='Shout of Power',
            game_text='Attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Scaly Uppercut',
            game_text='You may discard a Pokémon Tool card from this Pokémon. If you do, this attack does 90 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
